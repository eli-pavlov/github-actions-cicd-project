<div align='center'>
<img src="https://raw.githubusercontent.com/eli-pavlov/github-actions-cicd-project/master/docs/githubactions2.png" width=320 />
<h1> GitHub Actions CI/CD Project</h1>

<p> A complete GitOps-based Kubernetes CI/CD pipeline using GitHub Actions, Argo CD, Docker, SonarCloud, and Snyk. </p>

<h4>
  <span> · </span>
  <a href="https://github.com/eli-pavlov/github-actions-cicd-project/blob/master/README.md"> Documentation </a>
  <span> · </span>
  <a href="https://github.com/eli-pavlov/github-actions-cicd-project/issues"> Report Bug </a>
  <span> · </span>
  <a href="https://github.com/eli-pavlov/github-actions-cicd-project/issues"> Request Feature </a>
</h4>

$\~\~\$

</div>

## \:world\_map: Project Diagram

<img src="https://raw.githubusercontent.com/eli-pavlov/github-actions-cicd-project/master/docs/project-diagram.JPG" width="1000" />

$\~\~\$

\:notebook\_with\_decorative\_cover: Table of Contents

* [Project Diagram](#world_map-project-diagram)
* [About the Project](#star2-about-the-project)
* [CI/CD Workflow Overview](#gear-cicd-workflow-overview)
* [How to Set It Up](#wrench-how-to-set-it-up)
* [Project Structure](#open_file_folder-project-structure)
* [Secrets and Environments](#lock-secrets-and-environments)
* [License](#warning-license)
* [Contact](#handshake-contact)
* [Acknowledgements](#gem-acknowledgements)

$\~\~\$

## \:star2: About the Project

This project delivers an **end-to-end CI/CD pipeline** for a Python Flask web app.

**Key Features & Goals:**

* GitOps-driven continuous deployment using Argo CD and Kustomize overlays.
* **Semantic, unique Docker image tags** per deployment (e.g., `dev-abc1234`, `latest-abc1234`).
* Multi-stage CI/CD with linting, unit tests, code quality (SonarCloud), and security (Snyk).
* **Automatic updates to [manifests repo](https://github.com/eli-pavlov/github-actions-cicd-manifests)** to trigger deployments via Argo CD.
* Supports both automated dev deployments and manual-approval prod deployments.

**Why GitHub Actions?**

| Feature                      | Justification                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| 💰 **Cost-effective**        | Free for public repos, generous for private projects                                |
| 🔗 **Native Integration**    | Tight GitHub ecosystem fit: PRs, branches, commits, secrets                         |
| 🧰 **Rich Ecosystem**        | Thousands of actions for Docker, Argo CD, SonarCloud, Snyk, Slack, and more         |
| 👨‍💻 **Developer-Friendly** | Clean YAML, full commit history, branch-aware logic, easy rollbacks                 |
| 🔒 **Security**              | Encrypted secrets, support for environment approvals                                |
| ⚙️ **Scalable & Extensible** | Matrix jobs, reusable workflows, custom triggers, and environment-based deployments |

$\~\~\$

**Other tools used:**

* **GitOps:** [Argo CD](https://argo-cd.readthedocs.io/) for declarative Kubernetes deployment/version control.
* **Code Quality:** [SonarCloud](https://www.sonarcloud.io) for static analysis.
* **Security:** [Snyk](https://www.snyk.io) for IaC and dependency scanning.
* **Docker Hub** for image registry.

$\~\~\$

**Branching & Deployment Strategy:**

* `development`: Triggers full CI/CD pipeline, auto-deploys to development (K8s `development` namespace).
* `main`: Requires manual approval, deploys to production (`default` namespace).

$\~\~\$

## \:gear: CI/CD Workflow Overview

1. **Lint-and-Test**

   * Install dependencies, run `flake8`, execute unit tests with `pytest` + coverage.

2. **SonarCloud Analysis**

   * Perform static code analysis (using full git history).

3. **Snyk IaC Scan**

   * Scan Kubernetes manifests and Dockerfile for vulnerabilities.

4. **Build and Push Docker Image**

   * Build multi-arch Docker images (`dev-<sha>` or `latest-<sha>`).
   * Push image to Docker Hub.

5. **Update Manifests Repo (GitOps)**

   * Automatically update the correct overlay's `kustomization.yaml` in [github-actions-cicd-manifests](https://github.com/eli-pavlov/github-actions-cicd-manifests) with the new image tag.
   * Commit and push change.

6. **Argo CD Deployment**

   * Argo CD watches the manifests repo:

     * `/manifests/overlays/development` for dev
     * `/manifests/overlays/production` for prod
   * Syncs Kubernetes cluster with new image on change.

7. **Slack Notification (Optional)**

   * Post build/deploy status to Slack channel.

$\~\~\$

## \:wrench: How to Set It Up

### Prerequisites

* Fork or clone this repository.
* DockerHub account
* SonarCloud and Snyk accounts (optional, for quality/security)
* Kubernetes cluster with Argo CD installed and configured

### Steps

1. **Add required GitHub Secrets** (see [Secrets and Environments](#lock-secrets-and-environments)).
2. **Install Argo CD** on your cluster, if not already present.
3. **Apply Argo CD Applications** (see [manifests repo](https://github.com/eli-pavlov/github-actions-cicd-manifests)):

   ```bash
   kubectl apply -f manifests/argocd/application-dev.yaml
   kubectl apply -f manifests/argocd/application-prod.yaml
   ```
4. **Push to `development`**: triggers auto-deploy to dev environment.
5. **Merge to `main`**: requires approval and deploys to production.

$\~\~\$

## \:open\_file\_folder: Project Structure

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
├── docs/
│   ├── ci-cd-diagram-rtproject.pdf
│   ├── devops_cycle.jpg
│   ├── githubactions.png
│   ├── githubactions2.png
│   └── rtproject-diagram.png
├── manifests/
│   ├── base/             # Base K8s Deployment/Service (reference only)
│   ├── overlays/         # Overlays for dev and prod (reference only)
│   └── argocd/           # Argo CD App manifests (reference only)
└── .github/workflows/
    └── main.yml
```

> **Note:** Actual manifests for deployment are maintained in
> [github-actions-cicd-manifests](https://github.com/eli-pavlov/github-actions-cicd-manifests).

$\~\~\$

## \:lock: Secrets and Environments

> Add these secrets under **GitHub repo settings** → **Secrets and variables** → **Actions**

| Secret Key           | Description                           |
| -------------------- | ------------------------------------- |
| `APP_NAME`           | Docker image/app name                 |
| `DOCKERHUB_USERNAME` | Docker Hub username                   |
| `DOCKERHUB_TOKEN`    | Docker Hub token                      |
| `SONAR_TOKEN`        | SonarCloud token                      |
| `SONAR_ORGANIZATION` | SonarCloud organization               |
| `SONAR_PROJECT_KEY`  | SonarCloud project key                |
| `SNYK_TOKEN`         | Snyk token                            |
| `SLACK_WEBHOOK_URL`  | (Optional) Slack Incoming Webhook URL |
| `GH_TOKEN`           | Token for pushing to manifests repo   |

**GitHub Environments**:

* **development**: Auto-deploys on push to `development`.
* **production**: Requires manual approval before workflow runs for `main`.

$\~\~\$

## \:warning: License

Distributed under the Apache 2.0 License.

Please note: SonarCloud, Snyk, DockerHub, and Argo CD each have their own licensing terms.

$\~\~\$

## \:handshake: Contact

**Eli Pavlov**
[www.weblightenment.com](https://www.weblightenment.com)
[admin@weblightenment.com](mailto:admin@weblightenment.com)

Project Repo: [github-actions-cicd-project](https://github.com/eli-pavlov/github-actions-cicd-project)

$\~\~\$

## \:gem: Acknowledgements

* [Kubernetes.io](https://kubernetes.io/docs)
* [SonarCloud](https://www.sonarcloud.io)
* [Snyk](https://www.snyk.io)
* [DockerHub](https://hub.docker.com)
* [Argo CD](https://argo-cd.readthedocs.io/en/stable/)
* [GitHub Actions](https://docs.github.com/en/actions)
* [Awesome GitHub README Generator](https://www.genreadme.cloud/)
