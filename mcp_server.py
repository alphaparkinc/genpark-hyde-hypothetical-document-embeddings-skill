import sys
import json
from client import HyDEQueryExpander

expander = HyDEQueryExpander()

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-hyde-hypothetical-document-embeddings-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "expand_and_score_hyde",
                        "description": "Generate hypothetical document and score similarity against candidate text",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "query": {"type": "string", "description": "Input user search query"},
                                "candidate_text": {"type": "string", "description": "Candidate document text"}
                            },
                            "required": ["query", "candidate_text"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "expand_and_score_hyde":
            q = args.get("query", "")
            cand = args.get("candidate_text", "")
            pseudo = expander.generate_hypothetical_answer(q)
            v1 = expander.lexical_vector(pseudo)
            v2 = expander.lexical_vector(cand)
            sim = expander.cosine_similarity(v1, v2)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps({"hypothetical_doc": pseudo, "similarity": sim})}]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
