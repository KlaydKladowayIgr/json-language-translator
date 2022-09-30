# Json language file translator written in Python 3
## Uses
* Python 3 (3.5+)
* deep_translator
* tqdm
* json
* asyncio

## How to use
1. Edit `input.json` to add key:value pairs (key value is translated)
2. Run script
3. Enter target language
4. Wait for the end of the translation execution (accompanied by the result of the execution progress)
5. The finished translation of the json file is in `output.json`

## Example
`input.json`
```json
{
  "first_block": "First block",
  "second_block": "Second block",
  "third_block": "Third block"
}
```
`output.json`
```json
{
  "first_block": "Первый блок",
  "second_block": "Второй блок",
  "third_block": "Третий блок"
}
```
## Don't forget to install the dependencies (pip install -r requirements.txt)
