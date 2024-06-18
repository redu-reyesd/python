"""
Copyright [2009-present] EMBL-European Bioinformatics Institute
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
An example Python script showing how to access the public RNAcentral Postgres database.
Usage:
python example-rnacentral-postgres-script.py
"""


import psycopg2
import psycopg2.extras
from sub_modules.decrypt import decrypt_keys

def main():
    creds=decrypt_keys('./secure-passwords/rsa_keys/private-key.pem','./secure-passwords/rsa_keys/cfg.enc')
    conn_string = f"host={creds['hostname']} dbname={creds['database']} user={creds['user']} password={creds['password']}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # retrieve a list of RNAcentral databases
    query = "SELECT * FROM rnc_database"

    cursor.execute(query)
    for row in cursor:
        print(row)


if __name__ == "__main__":
    main()