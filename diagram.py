from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, Route53, CloudFront
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.database import Dynamodb
from diagrams.generic.device import Tablet, Mobile


graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("", graph_attr=graph_attr, show=False, direction='LR'):
    with Cluster(""):
      user_a = Tablet("Users")

      with Cluster("AWS"):
          
          with Cluster('CDN'):
            web_dns = Route53("Website DNS")
            web_cf = CloudFront("Website CloudFront")
            web_s3 = S3("Content S3 Bucket")

          with Cluster('API'):
            api_dns = Route53('API DNS')
            api_gateway = APIGateway("API Gateway")
            with Cluster("GET /"):
              data_lambda = LambdaFunction("Lambda Function")
              data_bucket = S3("Data S3 Bucket")
            with Cluster("GET /tags"):
              tags_lambda = LambdaFunction("Lambda Function")
              tags_table = Dynamodb("Tag Dynamo Table")
              

          with Cluster('Images'):
            images_bucket = S3("Images S3 Bucket")
            images_lambda = LambdaFunction("Lambda Function")

    user_a >> Edge(label="Access website", color="black") >> web_dns

    web_dns >> web_cf >> web_s3

    api_dns >> api_gateway

    api_gateway >> data_lambda >> data_bucket
    api_gateway >> tags_lambda >> tags_table

    web_dns >> Edge(label="Retrieve data") >> api_dns
    web_dns >> Edge(label="Retrieve images") >> images_bucket

    images_lambda >> Edge(label="resize and create thumbnail image") >> images_bucket
    images_bucket >> Edge(label="trigger when putting item") >> images_lambda