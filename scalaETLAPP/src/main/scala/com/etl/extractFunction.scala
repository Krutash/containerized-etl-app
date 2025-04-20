package com.etl

import org.apache.spark.sql.{DataFrame, SparkSession}

case class DBParams(url: String, user: String, password: String, driver: String, table: String)

object extractFunction{


  def extractFromDB(sparkSession: SparkSession, params: DBParams ): DataFrame = {

    sparkSession.conf.set("spark.hadoop.dfs.replication", "3")

    sparkSession.read
      .format("jdbc")
      .option("url", params.url)
      .option("user", params.user)
      .option("password", params.password)
      .option("dbTable", params.table)
      .option("driver", params.driver)
      .load()

  }

}
