resource "local_file" "kubeconfig" {
  depends_on   = [azurerm_kubernetes_cluster.cluster]
  filename     = "kubeconfig"
  content      = azurerm_kubernetes_cluster.cluster.kube_config_raw
}
resource "local_file" "kubeconfig_develop" {
  depends_on   = [azurerm_kubernetes_cluster.cluster_develop]
  filename     = "kubeconfig_develop"
  content      = azurerm_kubernetes_cluster.cluster_develop.kube_config_raw
}