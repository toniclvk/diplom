terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.48.0"
    }
  }
}
# Configure the Azure provider
provider "azurerm" {
  features {}
  subscription_id = var.azure-subscription-id
  client_id       = var.azure-client-id
  client_secret   = var.azure-client-secret
  tenant_id       = var.azure-tenant-id
}
# Postgres
resource "azurerm_resource_group" "postgresql-rg" {
  name     = "weather-postgresql-rg"
  location = "North Europe"
}
resource "azurerm_postgresql_server" "postgresql-server" {
  name = "database-lab2022-toniclvk"
  location = azurerm_resource_group.postgresql-rg.location
  resource_group_name = azurerm_resource_group.postgresql-rg.name
 
  administrator_login          = var.postgresql-admin-login
  administrator_login_password = var.postgresql-admin-password
 
  sku_name = var.postgresql-sku-name
  version  = var.postgresql-version
 
  storage_mb        = var.postgresql-storage
  auto_grow_enabled = true
  
  backup_retention_days        = 7
  geo_redundant_backup_enabled = false
  public_network_access_enabled     = true
  ssl_enforcement_enabled           = false
#  ssl_minimal_tls_version_enforced  = "TLS1_2"
}
resource "azurerm_postgresql_database" "postgresql-db" {
  name                = "weather01"
  resource_group_name = azurerm_resource_group.postgresql-rg.name
  server_name         = azurerm_postgresql_server.postgresql-server.name
  charset             = "utf8"
  collation           = "English_United States.1252"
}
resource "azurerm_postgresql_firewall_rule" "postgresql-fw-rule" {
  name                = "PostgreSQL_Office_Access"
  resource_group_name = azurerm_resource_group.postgresql-rg.name
  server_name         = azurerm_postgresql_server.postgresql-server.name
  start_ip_address    = "80.249.191.106"
  end_ip_address      = "80.249.191.111"
}
output "postgresql_server" {
  value = azurerm_postgresql_server.postgresql-server
  sensitive = true

}
# Kubernetes
resource "azurerm_resource_group" "rg" {
  name     = "toniclvk_k8s_ResourceGroup"
  location = "northeurope"
}

resource "azurerm_kubernetes_cluster" "cluster" {
  name                = "toniclvk_k8scluster"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "toniclvkk8scluster"

  default_node_pool {
    name       = "default"
    node_count = "2"
    vm_size    = "standard_d2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
  addon_profile {
    http_application_routing {
      enabled = true
    }
  }
}
