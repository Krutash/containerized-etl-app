package com.assignment;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.InputStreamReader;

@RestController
@RequestMapping("/etl")
public class ETLController {

    @PostMapping("/run")
    public String runETL(@RequestParam String tableName){
        String imageName = "spark-etl-app";
        try{

            ProcessBuilder pb = new ProcessBuilder(
                    //docker run --rm --network hadoop -e HOME=/tmp spark-etl-app users
                    "docker", "run", "--rm", "--network", "hadoop","-e","HOME=/root", imageName, tableName
            );

            pb.redirectErrorStream(true);

            Process p = pb.start();

            BufferedReader br = new BufferedReader(
                    new InputStreamReader(p.getInputStream())
            );

            StringBuilder output = new StringBuilder();
            String line;
            while((line = br.readLine()) != null){
                output.append(line).append("\n");
            }

            int exitCode = p.waitFor();

            return "ETL Job finished with exit code " + exitCode + ":\n" + output.toString();
        }
        catch (Exception e){
            e.printStackTrace();
            return "Failed to run ETL job: " + e.getMessage();
        }

    }

}
