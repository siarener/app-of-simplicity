# App of simplicity

This is a simple Python App, currently only logging the lorem-ipsum text. It's intention is to have a simple app for experimentation with DevOps, GitOps, etc. 

The real location of this project is in [GitLab](https://gitlab.com/siarener/app-of-simplicity), mirrored to [GitHub](https://github.com/siarener/app-of-simplicity). 

## Tasks done in this repository
1. Connecting GitHub and GitLab repositories
- Tried, did not work: Using GitLab CI pipelines for GitHub-hosted repositories by setting up a pull-mirror repository in GitLab (e.g. instructions [here](https://jhall.io/posts/github-with-gitlab-ci/)). This is no longer possible with a free-tier GitLab account.
- Currently, the GitLab repository simply has a push-mirror to the GitHub repository (steps see [here](./docs/gitlab_to_github_mirror.md))
- *ToDo*: Setting up a push-mirror in the GitHub repository to the GitLab repository, as the push-mirror is possible for free from the GitHub side. Check out the instructions [here](https://dev.to/brunorobert/github-and-gitlab-sync-44mn).