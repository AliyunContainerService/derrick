package common

type ParamReport struct {
	Name  string
	Nodes map[string]ParamReport
	Store map[string]string
}

func (dr *ParamReport) RegisterAutoParam(d AutoParam, nodeName string) error {
	node := dr.getNode(nodeName)
	if node.Store == nil {
		node.Store = map[string]string{}
	}
	result, err := d.Execute()
	if err != nil {
		return err
	}
	for k, v := range result {
		node.Store[k] = v
		dr.Store[k] = v
	}
	dr.Nodes[nodeName] = node
	return nil
}

func createNode(nodeName string) ParamReport {
	var report ParamReport
	report.Name = nodeName
	return report
}

func (dr *ParamReport) getNode(nodeName string) ParamReport {
	for _, i := range dr.Nodes {
		if i.Name == nodeName {
			return i
		}
	}
	return createNode(nodeName)
}

func (dr *ParamReport) GenerateReport() map[string]string {
	return dr.Store

}
