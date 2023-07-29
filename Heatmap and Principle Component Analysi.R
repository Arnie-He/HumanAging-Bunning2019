library(readxl)
library(pheatmap)

data <- read_excel("acel13073-sup-0002-tables1-s3.xlsx", sheet = "TableS3")
# head(data)

data_log <- log(data + 1)  # Adding 1 to handle zero values