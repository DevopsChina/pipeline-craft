?> In this task we will install `kubectl` to connect to the cluster, see https://kubernetes.io/docs/tasks/tools/

## Windows

```bash
choco install kubernetes-cli
# https://dl.k8s.io/release/v1.21.0/bin/windows/amd64/kubectl.exe
# Copy it as `k.exe` and add them to PATH, i.e. c:\tools\bin\
```

## Linux (Ubuntu)

```bash
snap install kubectl --classic
```

## MacOSX

```bash
brew install kubectl
```

## Setup shortcuts

Reference: https://kubernetes.io/docs/reference/kubectl/cheatsheet/

```bash
# MacOSX / Linux => BASH
echo 'source <(kubectl completion bash)' >>~/.bash_profile
echo 'alias k=kubectl' >>~/.bash_profile
echo 'complete -F __start_kubectl k' >>~/.bash_profile
source ~/.bash_profile

# ZSH
source <(kubectl completion zsh)
echo "[[ $commands[kubectl] ]] && source <(kubectl completion zsh)" >> ~/.zshrc
```

```PowerShell
# for Windows - PowerShell
# please add kubectl.exe and k.exe to PATH and restart PowerShell firstly
Set-Alias k kubectl

# permanent alias
# https://stackoverflow.com/questions/24914589/how-to-create-permanent-powershell-aliases
```

## Download config

1. Backup existing config
2. Write to `~/.kube/config`, create this file if not exists
3. Verify by `kubectl get node`, should return current nodes

```
$ k get nodes
NAME                   STATUS   ROLES    AGE   VERSION
pool-8eal681ba-8agl9   Ready    <none>   21m   v1.20.7
```
