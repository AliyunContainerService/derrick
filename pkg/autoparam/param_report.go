package autoparam

type ParamReport struct {
	templateData map[string]string
}

func NewParamReport() *ParamReport {
	return &ParamReport{
		templateData: make(map[string]string),
	}
}

func (dr *ParamReport) AddAutoParam(d AutoParam) error {
	result, err := d.Execute()
	if err != nil {
		return err
	}
	for k, v := range result {
		dr.templateData[k] = v
	}
	return nil
}

func (dr *ParamReport) TemplateData() map[string]string {
	return dr.templateData

}
