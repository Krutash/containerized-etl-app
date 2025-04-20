package com.etl

import org.apache.spark.sql.DataFrame

object loadDataIntoHDFS {

  def loadDataInHDFS(params: String, dataFrame: DataFrame): Unit = {
    dataFrame.write.mode("overwrite").parquet(s"hdfs://namenode:9000/data/${params}")
  }

}
