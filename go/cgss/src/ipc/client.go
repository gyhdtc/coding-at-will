package ipc

import (
	"encoding/json"
)

type IpcClient struct {
	conn chan string
}

func NewIpcClient(server *IpcServer) *IpcClient {
	c := server.Connect()
	return &IpcClient{c}
}

func (client *IpcClient)Call(method, params string) (resq *Response, err error) {
	req := &Request{method, params}
	var b []byte
	b, err = json.Marshal(req)
	if err != nil {
		return
	}
	client.conn <- string(b)
	var resp1 Response
	err = json.Unmarshal([]byte(str), &resp1)
	resp = &resp1

	return
}

func (client *IpcClient)Close() {
	client.conn <- "CLOSE"
}