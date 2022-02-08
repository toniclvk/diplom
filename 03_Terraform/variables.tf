variable "company" {
  description = "A prefix used for all resources in this example"
  default = "toniclvk"
}
variable "description" {
  description = "A prefix used for all resources in this example"
  default = "Deploy a PostgreSQL Server"
}
variable "owner" {
  description = "A prefix used for all resources in this example"
  default = "Kudryavtsev Vyacheslav"
}
variable "prefix" {
  description = "A prefix used for all resources in this example"
  default = "weather"
}

variable "location" {
  default     = "northeurope"
  description = "The Azure Region in which all resources in this example should be provisioned"
}

variable "postgresql-admin-login" {
  type        = string
  description = "Login to authenticate to PostgreSQL Server"
  default     = "weather"
}
variable "postgresql-admin-password" {
  type        = string
  description = "Password to authenticate to PostgreSQL Server"
  default     = ""
}
variable "postgresql-version" {
  type        = string
  description = "PostgreSQL Server version to deploy"
  default     = "11"
}
variable "postgresql-sku-name" {
  type        = string
  description = "PostgreSQL SKU Name"
  default     = "B_Gen5_1"
}
variable "postgresql-storage" {
  type        = string
  description = "PostgreSQL Storage in MB"
  default     = "5120"
}
variable "azure-subscription-id" {
  description = "The Azure subscription "
  default = ""
}
variable "azure-client-id" {
  description = "The Azure client-id "
  default = ""
}
variable "azure-client-secret" {
  description = "The Azure client-secret "
  default = ""
}
variable "azure-tenant-id" {
  description = "The Azure client-secret "
  default = ""
}
