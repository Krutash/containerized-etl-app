package com.etl

import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions._

object transformFunction {

  def transformInHDFS(dataFrame: DataFrame): DataFrame = {

    val newTransformedDataFrame =
      dataFrame.withColumn("day", lit((rand() * 30).cast("int") + 1))
        .withColumn("month", lit((rand()*12).cast("int")+1))
        .withColumn("year", lit((rand()*25).cast("int")+1))

    newTransformedDataFrame.withColumn("date", to_date(concat_ws("-", col("day"), col("month"), col("year")))).drop("day", "month", "year")

  }
}
