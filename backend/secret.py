import oci
import base64

def get_secret():
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    secret_client = oci.secrets.SecretsClient(config={}, signer=signer)

    response = secret_client.get_secret_bundle_by_name(
            secret_name="db_password",
            vault_id="ocid1.vault.oc1.uk-london-1.ert7hjwfaagii.abwgiljtnovczkov4qyoax4swcnxq3lig7wivwmy7urik4e6o35q5n33dejq")

    encoded_secret = response.data.secret_bundle_content.content
    secret = base64.b64decode(encoded_secret).decode("utf-8")
    return secret
