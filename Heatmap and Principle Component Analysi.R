library(readxl)
library(pheatmap)

data <- read_excel("acel13073-sup-0002-tables1-s3.xlsx", sheet = "TableS3")
# head(data)

# str(data)

# This will apply the log transformation to all rows except the first one (assuming it's the header)
data[, 2:ncol(data)] <- log(data[, 2:ncol(data)])

log_data <- data[, 2:ncol(data)]

# str(log_data)

library(pheatmap)

pheatmap(log_data, 
         main = "Natural Log-Transformed Metabolite Abundances",
         color = colorRampPalette(c("blue", "white", "red"))(100), 
         scale = "row", 
         clustering_distance_rows = "euclidean",
         clustering_distance_cols = "euclidean",
         clustering_method = "complete",
         # show_rownames = TRUE
)