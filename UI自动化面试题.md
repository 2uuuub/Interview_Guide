# UI自动化面试题目  
**1.UI自动化用例必须遵循哪些原则?**  
    第一:一个用例为一个完整的场景,例如从登录到退出,从打开到关闭;  
    第二:一个用例验证一个功能点;  
    第三:用例尽量做到覆盖主流程;
    第四:用例执行完成之后要对场景进行还原
    
**2.APP自动化环境需要搭建哪些服务?**  
    第一:jdk+node.js  
    第二:sdk  
    第三:appium,包括电脑端和移动端  
    第四:python+appium-python-client  
    
**3.完整介绍下你熟悉的自动化框架?**  
    自动化测试框架涵盖了基础方法封装,自定义异常封装,工具类封装,元素管理封装,po模型封装,日志封装,数据驱动封装.失败重试封装,浏览器/手机适配封装,数据库操作封装,测试用例管理封装,测试报告封装,通知邮件封装  
    初阶:编程语言-python  
        自动化模块工具-selenium/appium/requests  
        设计模式-po模型/关键字驱动  
    中阶:数据驱动-excel/yaml/json/data  
        测试用例-unitest/pytest  
        测试报告-htmltestrunner/allure  
        邮件模块-smtp  
    高阶:环境管理-服务器/数据库等  
        日志管理-logging  
        代码管理-git/svn  
        持续集成-jenkins  
        
**4.selenium如何获取页面标题?**  
    print("标题":driver.title)  
    
**5.用try语句写一个断言?**  
    try:  
       assert u"百度一下" in driver.title  
       print("测试通过")  
    except Exception as e:  
       print("测试失败",formatce)  
       
**6.selenium获取当前页面url?**  
    print("页面地址":driver.current_url)  
    
**7.selenium如何切换新打开的浏览器窗口?**  
    windows = driver.window_handles  
    driver.switch_to.window(windows[-1])  
    
**8.selenium如何设置浏览器窗口大小?**  
    driver.set_windows_size()  
    driver.maximize_window()  
    
**9.selenium如何切换新打开的浏览器窗口?**  
    windows = driver.window_handles  
    driver.switch_to.window(windows[-1])  
    
**10.selenium如何滚动页面?**  
    js_str = "scrollTo(0,5000)"  
    driver.execute_script(js_str)  
    
**11.selenium判断元素存在并可见?**  
    assert_element()  
    wait_for_element_visible()  
    
**12.写一个po模型实例?**  
    元素定位:  
    def get_element(self,*locator):  
        return self.driver.find_element(*locator)  
    点击元素:  
    def left_click(self,*locator):  
        ActionChains(self.driver).click(self.get_element(*locator)).perform()  
        
**13.简要说明一下3种等待方式?**  
    第一:固定等待  
    import time  
    time.sleep(10)  #强制等待10秒
    第二:隐式等待  
    driver.implicitly_wait(10)  #设置全局等待时间,10秒内若页面加载完成自动执行下一步  
    第三:显式等待-拿百度搜索举例
    import webdriver wait
    import expected_conditions  as ec
    wait = webdriverwait(driver,10,1) #10表示10秒超时,1表示每一秒刷新一次
    wait.until(ec.precence_of_element_located((by.id,"kw")))  #直到kw出现才执行下一步  
    
**14.selenium鼠标悬停如何操作?**  
    from selenium.webdriver.common.action_chains import ActionChains  
    ActionChains(driver).move_to_element(element).perform()  
    time.sleep(3)  #悬停三秒  
    
**15.H5小程序如何定位?**  
    第一:如果是微信小程序,在微信输入  debugx5qq.com,在信息栏勾选inspect调试  
    第二:如果是其他小程序,让开发打包时打开webdriver.debug权限  
    第三:开启usb调试模式并连接电脑,在谷歌浏览器打开调试网址chrome://inspect#devices  
    第四:点击inspect,打开页面,开始定位元素  
    
    

    
