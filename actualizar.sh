
jupyter nbconvert --execute covid-19-predictiva/Datalab/Datos_COVID-19_respaldo.ipynb
jupyter nbconvert --execute covid-19-predictiva/Datalab/Modelo_ARIMA_SIR.ipynb

jupyter nbconvert --to html covid-19-predictiva/Datalab/Datos_COVID-19_respaldo.ipynb
mv covid-19-predictiva/Datalab/Datos_COVID-19_respaldo.html covid-19-predictiva/Dashboard/SARS-COV-2/

jupyter nbconvert --to html covid-19-predictiva/Datalab/Modelos_ARIMA_SIR.ipynb
mv covid-19-predictiva/Datalab/Modelos_ARIMA_SIR.html covid-19-predictiva/Dashboard/SARS-COV-2/

cd covid-19-predictiva/Dashboard/SARS-COV-2
python3.7 jinja2_resultados.py

cd ../../..

cp -R covid-19-predictiva/Dashboard/SARS-COV-2 yoalvarezh.github.io

cd yoalvarezh.github.io
git add .
git commit -m "Actualización Dashboard"
git push origin

cd ..

cd covid-19-predictiva
git add .
git commit -m "Actualización Dashboard"
git push origin

cd ..