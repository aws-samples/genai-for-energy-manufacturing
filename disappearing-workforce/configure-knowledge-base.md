
# Configure the Knowledge base in Amazon Bedrock

Now comes the Knowledge base setup!

Lets setup the knowledge base in Amazon Bedrock.

1. In the AWS Management Console, use the search box at the top to search for Amazon Bedrock. Amazon Bedrock appears as the first option in the results, click on it to open the Bedrock console.

![Bedrock console](/static/disappearing-workforce/search-result-bedrock.png)

2. In the Amazon Bedrock console, click on the 3 horizontal lines in the top left corner to open the side menu.

3. Click on Knowledge Base under 'Orchestration' section.

![Orchestration](/static/disappearing-workforce/kb-bedrock.png)

4. Click on 'Create Knowledge Base'

![Create Knowledge Base](/static/disappearing-workforce/create-kb-bedrock.png)

1. In 'Provide knowledge base details' page, give the Knowledge base name as **bedrock-disappearing-workforce-kb**, under the 'IAM permissions' section, select "**Create and use a new service role**"  and click Next

2. Create S3 bucket and upload data/sample_pdfs folder
3. Enter the s3 directory where the files were uploaded. Do this by browsing the s3 location, selecting the s3 bucket and selecting the sample_pdfs folder. Then click Next

![s3 directory](/static/disappearing-workforce/S3-details-bedrock.png)
![s3 directory](/static/disappearing-workforce/S3-details-bedrock-folder.png)

1. In 'Select embeddings model and configure vector store' page, select Titan Embeddings G1 - Text model to provide embeddings to the data in 1536 dimensions. and under 'Vector database', select Quick create a new vector store - Recommended option. This uses OpenSearch serverless as the vector store by default and creates a new collection of vector search type. Then click Next

![embeddings model](/static/disappearing-workforce/vector-db-bedrock.png)

In 'Review and create' page, review all the settings and click Create Knowledge base

This will take few minutes to create a OpenSearch serverless collection as the vector database for your knowledge base.

8. After you've created your knowledge base, you can ingest the data sources into the knowledge base so that they are indexed and able to be queried. This is done with the "**Sync**" operation. When you sync a Bedrock knowledge base,the data in the S3 folder is chunked according to the setting you chose; embeddings are created for these chunks based on the chosen embeddings model and these embeddings along with some metadata are ingested in to an index inside an Amazon Opensearch serverless collection. Please note that this will take approximately "**10 minutes**" to ingest all the data from s3.
   
![embeddings model](/static/disappearing-workforce/sync-kb.png)

In this module, you set up a Bedrock knowledge base and synchronized the contents between s3 and the OpenSearch serverless collection. Bedrock has chunked your source data, generated the embeddings and stored them in an OpenSearch index.