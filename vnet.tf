provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "assign" {
  name     = "assign-resources"
  location = "East US"
}

resource "azurerm_virtual_network" "assign" {
  name                = "assign-vnet"
  address_space       = ["10.0.0.0/16"] 
  location            = azurerm_resource_group.assign.location
  resource_group_name = azurerm_resource_group.assign.name
}

resource "azurerm_subnet" "assign" {
  name                 = "assign-subnet"
  resource_group_name  = azurerm_resource_group.assign.name
  virtual_network_name = azurerm_virtual_network.assign.name
  address_prefixes     = ["10.0.1.0/24"] 
}
