# Sample Architecture Document

> This is an example of what your converted documentation will look like.
> 
> When you convert a PDF using `python convert_pdf.py pdfs/your-file.pdf`,
> the output will be a markdown file similar to this one.

---

## Example Content

Here's what a typical architecture document might contain after conversion:

### System Overview

This system consists of three main components:

1. **Frontend Application**
   - Built with React
   - Hosted on AWS CloudFront
   - Communicates with backend via REST API

2. **Backend Services**
   - Node.js/Express API server
   - Authentication via JWT tokens
   - Deployed on AWS ECS

3. **Database Layer**
   - PostgreSQL primary database
   - Redis for caching
   - Automated backups to S3

### Authentication Flow

1. User logs in with credentials
2. Backend validates against user database
3. JWT token issued with 24-hour expiration
4. Frontend stores token in secure httpOnly cookie
5. Token included in all API requests

### Infrastructure

- **Cloud Provider**: AWS
- **CDN**: CloudFront
- **Container Orchestration**: ECS
- **Database**: RDS PostgreSQL
- **Cache**: ElastiCache Redis
- **Storage**: S3

## How to Use This with Copilot

Once you have your actual documentation converted, you can ask Copilot questions like:

- "What authentication method is used?"
- "Describe the database architecture"
- "What cloud services are needed?"
- "How does the frontend communicate with the backend?"

Copilot will read this markdown content and provide accurate answers based on your specific documentation.
