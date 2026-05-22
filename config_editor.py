import json

with open('config.json', 'r') as f:
    config = json.load(f)

print(config)

key = input("你要修改哪个设置？(theme/language/font_size): ")

if key not in config:
    print(f"错误：'{key}' 不是有效的设置项")
else:
    value = input("新的值是什么？: ")
    if key == 'font_size':
        value = int(value)
        if value >= 8 and value <= 32:
            config[key] = value
            print(f"已更新: {key} = {value}")
        else:
            print("错误：字体大小必须在8到32之间")
    else:
        config[key] = value
        print(f"已更新: {key} = {value}")

with open('config.json', 'w') as f:
    json.dump(config, f)