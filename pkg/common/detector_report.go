package common

type ParamReport struct {
	Store map[string]string
}

func (dr *ParamReport) RegisterAutoParam(d AutoParam) error {
	result, err := d.Execute()
	if err != nil {
		return err
	}
	for k, v := range result {
		dr.Store[k] = v
	}
	return nil
}

func (dr *ParamReport) GenerateReport() map[string]string {
	return dr.Store

}
