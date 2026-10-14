---
title: "Publisher Owners, Managers and Contacts | Cat-Scan"
description: "Get publisher information from app stores, ads.txt, app-ads.txt, sellers.json and Google Marketplace. Identify source limits and save results."
---

# Publisher research

Cat-Scan gets current information about publisher owners, managers, seller accounts and business contacts.
You can use an app ID, a website domain or a company name.
Each result includes source URLs and the time of the lookup.

Use the API, the MCP tool or the CSV command for this function.
There is no publisher research screen or saved publisher directory.
The function does not select publishers by spend or contact companies.

## Information sources

| Source | Information | Limit |
|---|---|---|
| Google Play or Apple | Developer name and website | A developer is not necessarily the publisher owner. |
| `ads.txt` or `app-ads.txt` | Owner domain, manager domain and seller accounts | These are declarations from the website. |
| A declared manager's `sellers.json` | Business contacts and matching seller records | A match needs the advertising-system domain and the exact seller ID. |
| Google Marketplace | Visible publisher profiles and contacts for deals | Access depends on the buyer account and the service account. |

`OWNERDOMAIN` identifies the declared owner domain.
`MANAGERDOMAIN` identifies a declared manager domain.
Some manager declarations apply to a specified country.
The result keeps this country information.

A `DIRECT` seller entry identifies an account relationship.
The entry does not prove that the seller manages the publisher.
A Google parent profile does not prove a Google Multiple Customer Management relationship.
A company-name match is a possible association that needs more evidence.

A missing result means that the identity is unknown.
The sources do not prove exclusive rights or access through a buying route outside Google.
An app-store support address is not a verified advertising sales contact.

## Use Grok or another MCP client

The client must have an agent token with the `agent:publishers:read` permission.
The token must also give access to the selected buyer account.
See [MCP access](19-agent-access.md) and [Grok setup](20-grok-bot.md).

1. Ask the client to call `rtbcat_list_buyers`.
2. Select a buyer ID from the result.
3. Ask the client to call `rtbcat_lookup_publisher` with that buyer ID and the app ID or domain.
4. Examine the source URLs, `checked_at`, `partial` and truncation fields.
5. Keep unknown identities and source failures in your report.

For a company search, supply `publisher_name`.
For example, use `AnyMind` to find visible profiles with that name.
This search does not prove an association with a specified app.
An explicit company search takes precedence over automatic Google seller-account matching.

## Use the API

Send this example body to `POST /api/agent/v1/publisher-lookup` with an agent token.
Replace the buyer ID and app ID with the required values.

```json
{
  "buyer_id": "12345678",
  "app_id": "com.example.app",
  "include_google": true
}
```

Use an Android package name or a numeric Apple app ID for `app_id`.
Use `domain` instead of `app_id` for a website.
With both fields, `domain` overrides the developer website for the app.
The result marks this override as `provided_domain`.
It does not claim that the app store supplied the domain.

An authenticated app session can use `POST /api/publisher-lookup`.
The API applies the user's buyer permissions to this request.

## Process a CSV file

Use the Python environment in the platform repository.
The command below gets public evidence for each app ID in the input file.

```bash
venv/bin/python scripts/publisher_lookup.py \
  --input-csv /path/publishers.csv \
  --app-id-column 'Mobile app ID' \
  --output-json /path/publisher-evidence.json \
  --output-csv /path/publishers-enriched.csv
```

Add `--domain-column COLUMN` for a domain column.
Add `--buyer-id BUYER_ID --credentials /secure/service-account.json` for Google results.
With a buyer ID and no credentials file, the command uses Google Application Default Credentials.

The output CSV keeps the original columns and row sequence.
It adds columns for the evidence.
Rows without an app ID or domain remain in the output with `identity_required`.
The JSON file keeps the complete result within the lookup limits.
Credentials do not enter either output file.

## Google setup and limits

Enable `authorizedbuyersmarketplace.googleapis.com` in the service account's Google Cloud project.
Give that service account Marketplace access to the buyer account.
API activation alone does not give access to a buyer.

The API uses the buyer's linked active service account.
It does not substitute another customer's account if that link fails.
Public evidence can remain available when Google sends an error.

The lookup distinguishes an empty result from an authentication failure, a rejected query and a timeout.
For example, `no_visible_match` and `query_rejected` have different meanings.
Do not report a source failure as proof that a publisher does not exist.

The Google tests on 14 October 2026 found these results:

- Seller-code and company-name filters worked.
- The documented nested app filter was rejected.
- Domain filters gave HTTP 500.

Google profiles can omit apps, domains or contacts.
This function cannot reproduce every inventory association in the Authorized Buyers interface.

| Limit | Value |
|---|---|
| API lookup time | 12 seconds; completed sections can remain in a partial result |
| Declared managers with seller-file requests | 3 |
| Google `DIRECT` accounts used for automatic matching | 20 |
| Seller entries in the result | 500, with a total count and truncation flag |
| Google profile pages | 3 pages of up to 100 profiles |

The CSV command processes rows in sequence.
Store the output if you need a record of the lookup.
Cat-Scan does not automatically save these results as publisher records.

## References

- [Google publisher profile fields](https://developers.google.com/authorized-buyers/apis/marketplace/reference/rest/v1/buyers.publisherProfiles)
- [Google profile access and visibility](https://developers.google.com/authorized-buyers/apis/guides/marketplace/publisher-profiles)
- [IAB ads.txt and app-ads.txt specifications](https://iabtechlab.com/ads-txt/)
- [Platform implementation guide](https://github.com/jenbrannstrom/rtbcat-platform/blob/main/docs/PUBLISHER_LOOKUP.md)
