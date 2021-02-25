package common

type DetectorReport struct {
	CacheStore CacheStore
	Name       string
	Nodes      map[string]DetectorReport
	Store      map[string]string
}

func (dr *DetectorReport) RegisterDetector(d Detector, nodeName string) error {
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

func createNode(nodeName string) DetectorReport {
	var report DetectorReport
	report.Name = nodeName
	return report
}

func (dr *DetectorReport) getNode(nodeName string) DetectorReport {
	for _, i := range dr.Nodes {
		if i.Name == nodeName {
			return i
		}
	}
	return createNode(nodeName)
}

func (dr *DetectorReport) GenerateReport() map[string]string {
	//return recursiveGenerateStore(*dr)
	return dr.Store

}

func recursiveGenerateStore(dr DetectorReport) map[string]string {
	nodes := dr.Nodes
	store := dr.Store
	if len(nodes) > 0 {
		for _, v := range nodes {
			s := recursiveGenerateStore(v)
			for i, j := range s {
				store[i] = j
			}
		}
	}
	return store
}
