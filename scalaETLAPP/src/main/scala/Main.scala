import com.typesafe.config.ConfigFactory
import org.apache.spark.sql.SparkSession

import com.etl.extractFunction
import com.etl._

object Main {
  def main(args: Array[String]): Unit = {

    if (args.length != 1) {
      println("Error in Usage: ETL expects <table_name>")
      sys.exit(1)
    }

    val config = ConfigFactory.load("application.conf")  // or pass path explicitly
    val dbConfig = config.getConfig("db")

    val params = DBParams(
      url =  dbConfig.getString("url"),
      user = dbConfig.getString("user"),
      password = dbConfig.getString("password"),
      driver = dbConfig.getString("driver"),
      table = args(0)
    )

    val sparkSession = SparkSession.builder()
      .appName("Modular ETL")
      .master("local[*]")
      .getOrCreate()

    val extractedDF = extractFunction.extractFromDB(sparkSession, params)

    extractedDF.show()

    val transformedDF = transformFunction.transformInHDFS(extractedDF)

    loadDataIntoHDFS.loadDataInHDFS(params.table, transformedDF)

    println("Success")
    sparkSession.stop()

  }
}
