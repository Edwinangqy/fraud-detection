from evidently.report import Report
from evidently.metrics import DataDriftPreset
import pandas as pd

ref = pd.read_csv("monitor/ref.csv")
new = pd.read_csv("monitor/new.csv")

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=new)
report.save_html("monitor/report.html")
