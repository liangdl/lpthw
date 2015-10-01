# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", # 这个string里面有个'号，所以出来的结果会变成双引号
	"So I said goodnight."
)
	