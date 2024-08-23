
# Amazon Bedrock setup

We will be using Amazon [Bedrock](https://aws.amazon.com/bedrock/) to access foundation models in this workshop.

Below we will configure model access in Amazon Bedrock in order to build and run generative AI applications. Amazon Bedrock provides a variety of foundation models from several providers.

# Amazon Bedrock setup instructions
1. Find Amazon Bedrock by searching in the AWS console.
 
 ![Search for Bedrock service](/static/bedrock/bedrock-search.png)

2. Expand the side menu.
   
 ![Expand the side menu](/static/bedrock/bedrock-menu-expand.png)

3. From the side menu, select Model access.
 
 ![Select Model access](/static/bedrock/model-access-link.png)

4. Select the "**Enable specific model**" or "**Modifiy model access** button.
   
 ![Select the Manage model](/static/bedrock/model-access-view-subset.png)

5. Select the checkboxes listed below to activate the models. If running from your own account, there is no cost to activate the models - you only pay for what you use during the labs. Review the applicable EULAs as needed.

- Amazon (select Amazon to automatically select all Amazon Titan models)
- Anthropic > Claude 3 Sonnet, Claude and Claude Instant
- Meta > Llama 3 8B Instruct
- Mistral AI > Mistral Large
 
Click "**Next**" to activate the models in your account.

![Select the Manage model](/static/bedrock/model-access-select.png)

1. Review and submit your models
   
![Select the Manage model](/static/bedrock/model-submit.png)

7. Monitor the model access status. It may take a few minutes for the models to move from In Progress to Access granted status. You can use the Refresh button to periodically check for updates.

8. Verify that the model access status is Access granted for the previously selected models.
   
![Select the Manage model](/static/bedrock/model-access-complete-subset.png)
