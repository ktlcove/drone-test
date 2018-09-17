FROM python
ADD ${CI_WORKSPACE}/* /code
WORKDIR /code
RUN pip install .

EXPOSE 5000

CMD ["python", "-m", "drone_test.app"]