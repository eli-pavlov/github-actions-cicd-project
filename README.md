<div align='center'>
<img src="https://raw.githubusercontent.com/eli-pavlov/github-actions-cicd-project/master/docs/githubactions2.png" width=320 />
<h1> GitHub Actions CI/CD Project</h1>

<p> A complete GitOps-based Kubernetes CI/CD pipeline using GitHub Actions, Argo CD, Docker, SonarCloud, and Snyk. </p>

<h4> <span> · </span> <a href="https://github.com/eli-pavlov/github-actions-cicd-project/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/eli-pavlov/github-actions-cicd-project/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/eli-pavlov/github-actions-cicd-project/issues"> Request Feature </a> </h4>

~~~

</div>

## Project Diagram

<img src="https://github.com/eli-pavlov/github-actions-cicd-project/blob/master/docs/rtproject-diagram.png" width=1080 />

~~~

## Table of Contents

* [Project Diagram](#project-diagram)
* [About the Project](#about-the-project)
* [CI/CD Workflow Overview](#cicd-workflow-overview)
* [How to Set It Up](#how-to-set-it-up)
* [Project Structure](#project-structure)
* [Secrets and Environments](#secrets-and-environments)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

~~~

## About the Project

This project delivers a production-grade CI/CD pipeline for a Python Flask web app, as part of a DevOps internship assignment.

**Goals:**

* Implement modern CI/CD practices using GitHub Actions.
* Support both development and production deployment workflows.
* Enforce code quality and security via SonarCloud and Snyk.
* Deploy to Kubernetes clusters via GitOps using Argo CD.
* Apply semantic Docker image tagging based on branch.

**Key Decisions:**

**CI Tool: GitHub Actions**

GitHub Actions was selected for its integration, ecosystem, and simplicity. Here’s why:

- **Cost-effective**: Free for public repos, generous private repo tier.
- **Native GitHub Integration**: Tightly integrated with PRs, branches, commits — no external setup needed.
- **Rich Ecosystem**: Thousands of prebuilt actions on the [GitHub Marketplace](https://github.com/marketplace/actions) for Docker, SonarCloud, Argo CD, and more.
- **Developer-Friendly**: YAML-based config with commit history, rollback, and branch logic.
- **Security**: Secure secrets management and support for [GitHub Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments) with approval gates.
- **Scalability & Extensibility**: Supports parallel jobs, matrix builds, reusable workflows, and various event triggers.

This makes GitHub Actions the best choice for:
- A fully automated CI/CD pipeline.
- Clear visibility in the GitHub UI.
- Minimal external tooling/setup.

**Other tools used:**

* Argo CD — Declarative Kubernetes deployment (GitOps).
* SonarCloud — Static code analysis.
* Snyk — Security scanning of IaC and Dockerfiles.

**Branching Strategy:**

* `development`: Triggers full CI/CD pipeline and auto-deploys to development.
* `main`: Requires manual approval and deploys to production via Argo CD.

~~~

## CI/CD Workflow Overview

### 1. Lint and Test

- Installs dependencies.
- Runs `flake8` for linting.
- Runs unit tests using `pytest` and generates a coverage report.

### 2. SonarCloud Analysis

- Performs static code quality scanning using SonarCloud.
- Uses a GitHub Action with appropriate secrets for secure access.

### 3. Snyk IaC Scan

- Scans Kubernetes manifests and the Dockerfile for security vulnerabilities.
- Failures are ignored to allow review and not block the pipeline.

### 4. Build and Push Docker Image

- Builds multi-architecture images using QEMU and Buildx.
- Tags:
  - `dev` for development branch
  - `latest` for main (production) branch
- Pushes the image to Docker Hub.

### 5. Argo CD Deployment

- Development: Auto-deploys after code is pushed to the `development` branch.
- Production: Deploys after push to `main`, but requires manual approval.
- Argo CD monitors the correct Kustomize overlay path:
  - `/manifests/overlays/development`
  - `/manifests/overlays/production`

### 6. Slack Notification (Optional)

- Sends build and deployment status notifications to Slack using a webhook.

~~~

## How to Set It Up

### Prerequisites:

- GitHub repository
- DockerHub account
- SonarCloud and Snyk accounts (optional)
- Kubernetes cluster with Argo CD installed and configured

### Steps:

1. Fork or clone this repository.
2. Add GitHub Secrets (see [Secrets and Environments](#secrets-and-environments)).
3. Install Argo CD on your Kubernetes cluster (or use an existing one).
4. Apply the Argo CD applications:

   ```bash
   kubectl apply -f manifests/argocd/application-dev.yaml
   kubectl apply -f manifests/argocd/application-prod.yaml
   ```

5. Push to `development` to auto-deploy to the dev environment.
6. Merge to `main` and approve via GitHub Environment to deploy to production.

~~~

## Project Structure

```
github-actions-cicd-project/
├── Dockerfile
├── README.md
├── requirements.txt
├── src/
│   ├── app.py
│   ├── __init__.py
│   └── templates/index.html
├── tests/test_app.py
├── manifests/
│   ├── base/             # Base Kubernetes Deployment/Service
│   ├── overlays/
│   │   ├── development/  # Patched for dev (nodePort 30070)
│   │   └── production/   # Patched for prod (nodePort 30080)
│   └── argocd/           # Argo CD Application manifests
├── docs/
│   ├── *.png/pdf
└── .github/workflows/main.yml
```

~~~

## Secrets and Environments

> Add these secrets under **GitHub repo settings** > **Secrets and variables** > **Actions**

Secrets to set:

- `APP_NAME`: Docker image/app name
- `DOCKERHUB_USERNAME`: Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub token
- `SONAR_TOKEN`: SonarCloud token
- `SONAR_ORGANIZATION`: SonarCloud organization
- `SONAR_PROJECT_KEY`: SonarCloud project key
- `SNYK_TOKEN`: Snyk token
- `SLACK_WEBHOOK_URL`: (Optional) Slack webhook for notifications

GitHub Environments:

- **development**: Auto-deploys when code is pushed to `development`.
- **production**: Requires manual approval before deployment (configured in GitHub).

~~~

## License

Distributed under the Apache 2.0 License.

Please note: SonarCloud, Snyk, DockerHub, and Argo CD each have their own licensing terms.

~~~

## Contact

**Eli Pavlov**  
[www.weblightenment.com](https://www.weblightenment.com)  
[admin@weblightenment.com](mailto:admin@weblightenment.com)  

Project Repo: [github-actions-cicd-project](https://github.com/eli-pavlov/github-actions-cicd-project)

~~~

## Acknowledgements

- [Kubernetes.io](https://kubernetes.io/docs)
- [SonarCloud](https://www.sonarcloud.io)
- [Snyk](https://www.snyk.io)
- [DockerHub](https://hub.docker.com)
- [Argo CD](https://argo-cd.readthedocs.io/en/stable/)
- [Awesome GitHub README Generator](https://www.genreadme.cloud/)
