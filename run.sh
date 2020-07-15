export PYTHONPATH=/pyimgur

echo "Executing tests..."

python -m pytest -v -s tests/ --html=/report/report.html

echo "Please check report.html at /tmp/report"
