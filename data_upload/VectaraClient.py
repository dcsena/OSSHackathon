import json
import logging
import requests

API_ENDPOINT = "https://api.vectara.io"
class VectaraClient:
    def __init__(self, customer_id, corpus_id, api_key):
        self.customer_id = customer_id
        self.corpus_id = corpus_id
        self.api_key = api_key

    @staticmethod
    def construct_document(job_id, job_title, raw_jd, metadata):
        return {
            "documentId": job_id,
            "title": job_title,
            "description": raw_jd,
            "metadataJson": json.dumps(metadata),
            "section": []
        }
    def index_document(self, document):
        """Indexes content to the corpus.

        Args:
            document: Document to index

        Returns:
            (response, True) in case of success and returns (error, False) in case of failure.
        """
        post_headers = {
            "x-api-key": f"{self.api_key}",
            "customer-id": f"{self.customer_id}",
            "Content-Type": "application/json"
        }
        print(document)
        print(json.dumps(document))
        response = requests.post(
            f"https://{API_ENDPOINT}/v1/index",
            data=document,
            verify=True,
            headers=post_headers)

        if response.status_code != 200:
            logging.error("REST upload failed with code %d, reason %s, text %s",
                           response.status_code,
                           response.reason,
                           response.text)
            return response, False

        message = response.json()
        if message["status"] and message["status"]["code"] not in ("OK", "ALREADY_EXISTS"):
            logging.error("REST upload failed with status: %s", message["status"])
            return message["status"], False

        return message, True