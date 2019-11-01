// 日志对外接口
// 本例中定义一个日志写入器接口（LogWriter），要求写入设备必须遵守这个接口协议才能被日志器（Logger）注册。
// 日志器有一个写入器的注册方法（Logger 的 RegisterWriter() 方法）。
// 日志器还有一个 Log() 方法，进行日志的输出，这个函数会将日志写入到所有已经注册的日志写入器（LogWriter）中。
package main

import "fmt"

type LogWriter interface {
	Write(data interface{}) error
}

type Logger struct {
	writelist []Logger
}

func (l *Logger) RegisterWriter(writer LogWriter) {
	l.writelist = append(l.writelist, writer)
}

// 将一个data类型的数据写入日志
func (l *Logger) Log(data interface{}) {
	for _, writer := range l.writelist {
		writer.Write(data)
	}
}

// 创建日志器的实例
func NewLogger() *Logger {
	return &Logger{}
}