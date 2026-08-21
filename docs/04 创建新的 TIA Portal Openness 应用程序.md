# 4 创建一个新的 TIA Portal Openness 应用程序

## 4.1 TIA Portal V17.0

安装 TIA Portal V17.0。

!!! note
在 STEP 7 V17.0 或 WinCC V17.0 中，TIA Portal Openness V17.0 包含在交付范围内，并默认随其一同安装。


## 4.2 管理用户权限

要使用和/或创建 TIA Portal Openness 应用程序，必须将该用户添加到“Siemens TIA Openness”用户组中。


表 4-1
| 编号 | 操作 |
|------|------|
| 1. | 在 Windows 任务栏上右键单击“开始”（Windows）图标。选择“计算机管理”，然后单击“确定”以确认用户账户控制（UAC）对话框中的提示。![alt text](image-2.png)|
| 2. | 打开“本地用户和组>用户”然后双击用户名“OpennessUser”。 ![alt text](image.png)|
| 3. | 切换到“所属”选项卡，然后点击“添加...”按钮。![alt text](image-3.png)|
| 4. | 输入“Siemens TIA Openness”，然后单击“确定”进行确认。![alt text](image-4.png)|
| 5. | 关闭所有打开的对话框，然后重新登录。|


## 4.3 创建项目

表 4-2

| 编号 | 操作 |
|------|------|
| 1. | 创建一个新项目（例如在 Microsoft Visual Studio 中）。 |
| 2. | 创建对 Openness DLL（Siemens.Engineering.dll 和 Siemens.Engineering.HMI.dll）的引用。 它们位于 TIA Portal 安装目录下的“... > Siemens > Automation > Portal V17_0 > PublicAPI > V17.0”中。 |
| 3. | 将这两个 DLL 的“Copy Local”属性设置为“False”。![alt text](image-1.png) |

## 4.4 配置文件 / AssemblyResolve

要查找 Openness DLL 的路径，您可以使用配置文件或“AssemblyResolve”事件。

表4-3

| 编号 | 操作 |
|------|------|
| 1. | 配置文件：如果您在安装 STEP 7 V17.0 或 WinCC V17.0 (TIA Portal) 时选择了与默认路径不同的路径，请在配置文件中将默认路径替换为您实际的安装路径。请在与 Openness 应用程序相同的目录下创建应用程序配置文件。 |
| 2. | AssemblyResolve要建立与 TIA Portal 的连接，可以使用 Resolver.GetAssemblyPath 方法。该方法会从注册表中读取 TIA Portal 的安装路径，从而使程序能够独立于安装路径运行。 |

## 4.5 授予访问权限


表 4-4

| 编号 | 操作 |
|------|------|
| 1. |首次启动该应用程序时，会显示以下安全提示：![alt text](image-5.png)  来源:[系统手册(https://support.industry.siemens.com/cs/ww/en/view/109477163)](https://support.industry.siemens.com/cs/ww/en/view/109477163)|
| 2. |点击“是”确认该消息，以允许一次性访问。点击 “是，全部”确认该消息，以始终允许该应用程序访问。点击“否”以拒绝访问。|


!!! note
如果您正在使用 Microsoft Visual Studio，即使您已经点击了"全部是"，仍可能会收到该安全提示。请按照第 5 章所引用的文章中的说明操作，以避免出现这种情况。

