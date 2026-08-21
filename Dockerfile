FROM python:3.11-slim
WORKDIR /app
RUN pip install biopython
COPY parser_with_errorhandling.py .
CMD ["python", "parser_with_errorhandling.py"]
