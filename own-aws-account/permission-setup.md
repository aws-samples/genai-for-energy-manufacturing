
# Minimum IAM permissions (for system admins)

You can run this workshop with the default Administrator role.

If you need minimum permissions enabled for participants, here is the required policy JSON:

As an administrator, you will need to create one Cloud9 environment in the account to automatically create some required service roles needed for the workshop users. See [AWS Cloud9 setup instructions here](/own-aws-account/cloud9-setup). You can then immediately delete the Cloud9 environment you created as an administrator.

```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"cloud9:CreateEnvironmentSSH",
				"cloud9:CreateEnvironmentEC2"
			],
			"Resource": "*",
			"Condition": {
				"Null": {
					"cloud9:OwnerArn": "true"
				}
			}
		},
		{
			"Sid": "VisualEditor1",
			"Effect": "Allow",
			"Action": "cloud9:GetUserPublicKey",
			"Resource": "*",
			"Condition": {
				"Null": {
					"cloud9:UserArn": "true"
				}
			}
		},
		{
			"Sid": "VisualEditor2",
			"Effect": "Allow",
			"Action": "cloud9:DescribeEnvironmentMemberships",
			"Resource": "*",
			"Condition": {
				"Null": {
					"cloud9:UserArn": "true",
					"cloud9:EnvironmentId": "true"
				}
			}
		},
		{
			"Sid": "VisualEditor3",
			"Effect": "Allow",
			"Action": [
				"ssm:GetConnectionStatus",
				"cloud9:TagResource",
				"cloud9:GetUserSettings",
				"iam:ListRoles",
				"ssm:StartSession",
				"iam:ListInstanceProfilesForRole",
				"cloud9:ListEnvironments",
				"cloud9:DescribeEnvironments",
				"cloud9:ListTagsForResource",
				"ec2:DescribeInstanceTypeOfferings",
				"ec2:DescribeVpcs",
				"iam:ListUsers",
				"iam:GetUser",
				"cloud9:UpdateUserSettings",
				"ec2:DescribeSubnets",
				"ec2:DescribeRouteTables"
			],
			"Resource": "*"
		},
		{
			"Sid": "VisualEditor4",
			"Effect": "Allow",
			"Action": "iam:CreateServiceLinkedRole",
			"Resource": "*",
			"Condition": {
				"StringLike": {
					"iam:AWSServiceName": "cloud9.amazonaws.com"
				}
			}
		},
		{
			"Sid": "VisualEditor5",
			"Effect": "Allow",
			"Action": [
				"ssm:GetConnectionStatus",
				"ssm:StartSession"
			],
			"Resource": "arn:aws:ec2:::instance/*",
			"Condition": {
				"StringEquals": {
					"aws:CalledViaFirst": "cloud9.amazonaws.com"
				},
				"StringLike": {
					"ssm:resourceTag/aws:cloud9:environment": ""
				}
			}
		},
		{
			"Sid": "VisualEditor6",
			"Effect": "Allow",
			"Action": "ssm:StartSession",
			"Resource": [
				"*"
			]
		},		
		{
			"Sid": "BedrockExecutionRolePolicy",
            "Effect": "Allow",
            "Action": [
                "iam:CreatePolicy",
                "iam:AttachRolePolicy",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/AmazonBedrockExecutionRoleForKnowledgeBase_DisappearingWorkforce"
            ]
        },
		{
			"Sid": "QuicksightPolicy",
			"Effect": "Allow",
			"Action": [
				 "quicksight:subscribe",
                "quicksight:CreateAdmin",
                "quicksight:CreateAccountSubscription",
                "quicksight:CreateAnalysis",
                "quicksight:CreateDashboard",
                "quicksight:CreateDataSource",
                "quicksight:CreateDataSet",
                "quicksight:CreateIAMPolicyAssignment",
                "quicksight:CreateRoleMembership",
                "quicksight:CreateTopic",
                "quicksight:CreateTopicRefreshSchedule",
                "quicksight:DescribeAccountSettings",
                "quicksight:DescribeAccountSubscription",
                "quicksight:DescribeAnalysis",
                "quicksight:DescribeDashboard",
                "quicksight:DescribeDataSet",
                "quicksight:DescribeDataSource",
                "quicksight:DescribeTopic",
                "quicksight:DescribeUser",
                "quicksight:ListAnalyses",
                "quicksight:ListDashboards",
                "quicksight:ListDashboardVersions",
                "quicksight:ListDataSets",
                "quicksight:ListDataSources",
                "quicksight:ListIAMPolicyAssignments",
                "quicksight:ListIAMPolicyAssignmentsForUser",
                "quicksight:ListRoleMemberships",
                "quicksight:ListTopics",
                "quicksight:ListUsers",
                "quicksight:RegisterUser",
                "quicksight:SearchAnalyses",
                "quicksight:SearchDashboards",
                "quicksight:SearchDataSets",
                "quicksight:UpdateAccountSettings",
                "quicksight:UpdateAnalysis",
                "quicksight:UpdateTopic",
                "quicksight:UpdateUser",
                "quicksight:CreateUser",
                "quicksight:UpdateDashboard",
                "quicksight:UpdateDataSet",
                "quicksight:UpdateDataSource",
                "quicksight:UpdateGroup",
                "quicksight:UpdateResourcePermissions",
                "ds:CreateIdentityPoolDirectory",
                "ds:CheckAlias",
                "ds:DescribeDirectories",
                "ds:DescribeTrusts",
                "ds:DeleteDirectory",
                "ds:CreateAlias",
                "ds:UnauthorizeApplication",
                "ds:AuthorizeApplication"
			],
			"Resource": [
				"*"
			]
		},
		{
			"Sid": "BedrockPolicy",
			"Effect": "Allow",
			"Action": [
				"bedrock:GetFoundationModelAvailability",
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:PutFoundationModelEntitlement",
                "bedrock:PutUseCaseForModelAccess",
                "bedrock:GetUseCaseForModelAccess",
                "bedrock:CreateFoundationModelAgreement",
				"bedrock:CreateKnowledgeBase",
				"bedrock:GetDataSource",
				"bedrock:CreateDataSource",
				"bedrock:GetKnowledgeBase",
				"bedrock:StartIngestionJob",
				"bedrock:GetIngestionJob",
				"bedrock:RetrieveAndGenerate",
				"bedrock:Retrieve",
				"bedrock:List*",
				"aoss:BatchGetCollection",
                "aoss:CreateAccessPolicy",
                "aoss:CreateCollection",
                "aoss:CreateSecurityPolicy",
                "aoss:ListCollections",
                "aoss:APIAccessAll"
			],
			"Resource": "*"
		},	
		{
			"Sid": "BedrockModelRestrictionPolicy",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:Subscribe"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws-marketplace:ProductId": [
                        "prod-6dw3qvchef7zy",
						"prod-nb4wqmplze2pm",
						"prod-ariujvyzvd2qy",
						"prod-m5ilt4siql27k",
						"prod-tukx4z3hrewle",
						"b7568428-a1ab-46d8-bab3-37def50f6f6a",
						"b0eb9475-3a2c-43d1-94d3-56756fd43737",
						"c468b48a-84df-43a4-8c46-8870630108a7",
						"a61c46fe-1747-41aa-9af0-2e0ae8a9ce05",
						"216b69fd-07d5-4c7b-866b-936456d68311"
                    ]
                }
            }
        },
        {
			"Sid": "MarketplaceSubscriptions",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:Unsubscribe",
                "aws-marketplace:ViewSubscriptions"
            ],
            "Resource": "*"
        },
		{
            "Sid": "qbusinessPolicy",
            "Effect": "Allow",
            "Action": [
                "qbusiness:*",
				"sso:*",
				"sso-directory:*",
				"user-subscriptions:*",
                "identitystore:DescribeGroup",
                "identitystore:DescribeUser",
                "identitystore:IsMemberInGroups",
                "identitystore:ListGroupMemberships"
            ],
            "Resource": [
                "*"
            ]
        }
	]
}
```