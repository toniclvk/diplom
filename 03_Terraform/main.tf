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
  name     = "toniclvk_weather-postgresql-rg"
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
resource "azurerm_postgresql_database" "postgresql-db-dev" {
  name                = "weather02"
  resource_group_name = azurerm_resource_group.postgresql-rg.name
  server_name         = azurerm_postgresql_server.postgresql-server.name
  charset             = "utf8"
  collation           = "English_United States.1252"
}
resource "azurerm_postgresql_firewall_rule" "postgresql-fw-rule" {
  name                = "PostgreSQL_any_Access"
  resource_group_name = azurerm_resource_group.postgresql-rg.name
  server_name         = azurerm_postgresql_server.postgresql-server.name
  start_ip_address    = "0.0.0.0"
  end_ip_address      = "255.255.255.255"
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
resource "azurerm_log_analytics_workspace" "prodaction" {
  name                = "k8s-workspace-prodaction"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}
resource "azurerm_log_analytics_workspace" "develop" {
  name                = "k8s-workspace-develop"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}
resource "azurerm_kubernetes_cluster" "cluster" {
  name                = "toniclvk_k8scluster_prodaction"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "toniclvkk8scluster"

  default_node_pool {
    name       = "default"
    vm_size    = "standard_d2_v2"
    enable_auto_scaling = true
    node_count = "2"
    min_count = "1"
    max_count = "3"
    max_pods = "110"
  }

  identity {
    type = "SystemAssigned"
  }
  addon_profile {
    http_application_routing {
      enabled = true
    }
    oms_agent {
      enabled                    = true
      log_analytics_workspace_id = "${azurerm_log_analytics_workspace.prodaction.id}"
    }
  }
  auto_scaler_profile {
    scale_down_delay_after_add       = "5m"
  }
}
resource "azurerm_kubernetes_cluster" "cluster_develop" {
  name                = "toniclvk_k8scluster_develop"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "toniclvkk8sclusterdev"

  default_node_pool {
    name       = "default"
    vm_size    = "standard_d2_v2"
    enable_auto_scaling = true
    node_count = "2"
    min_count = "1"
    max_count = "3"
    max_pods = "110"
  }

  identity {
    type = "SystemAssigned"
  }
  addon_profile {
    http_application_routing {
      enabled = true
    }
    oms_agent {
      enabled                    = true
      log_analytics_workspace_id = "${azurerm_log_analytics_workspace.develop.id}"
    }
  }
}
