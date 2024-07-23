
# Multilingual Movie Information Chatbot

Welcome to the Multilingual Movie Information Chatbot! This project is a serverless, multi-language chatbot that provides movie information to users. It leverages the power of Large Language Models (LLMs) to deliver accurate and insightful responses. The chatbot is deployed on AWS Fargate and uses several modern technologies to ensure scalability, reliability, and efficient data handling.

## Features

- **Multi-language Support**: The chatbot can interact with users in multiple languages, making it accessible to a global audience.
- **Serverless Architecture**: Leveraging AWS Fargate for seamless scaling and management.
- **Advanced Search Capabilities**: Utilizes Qdrant vector database for efficient storage and retrieval of user queries.
- **Monitoring and Logging**: Uses AWS CloudWatch for comprehensive logging and monitoring.
- **Load Balancing**: Deployed with a load balancer for handling high traffic and ensuring smooth performance.
- **Prompt Engineering**: Uses CometML to optimize prompt development and ensure high-quality interactions.

## Architecture Overview

1. **AWS Fargate**: Provides serverless compute capacity, enabling the chatbot to scale automatically without managing servers.
2. **Qdrant Vector Database**: Stores vector representations of user queries, enabling efficient similarity search and retrieval.
3. **AWS CloudWatch**: Monitors application performance and logs, helping to quickly identify and resolve issues.
4. **Load Balancer**: Distributes incoming traffic across multiple instances, ensuring high availability and reliability.
5. **CometML**: Facilitates prompt engineering and experiment tracking for LLM development.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

