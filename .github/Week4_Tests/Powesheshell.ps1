
#Get-AzVM -ResourceGroupName FinanceEast -Name 'QTC-APP123'

$rg="learn-quickstart-vm-rg"

New-AzResourceGroupDeployment -Name CanekVm1 -ResourceGroupName $rg -TemplateUri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-windows/azuredeploy.json" `
                                -adminUsername canekadmin -dnsLabelPrefix mydeployment-31926

Get-AzResourceGroupDeployment -Name CanekVm1 -ResourceGroupName $rg