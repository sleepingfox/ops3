from django.db import models

# Create your models here.


ASSET_STATUS = (
    (str(1), u"使用中"),
    (str(2), u"未使用"),
    (str(3), u"故障"),
    (str(4), u"其它"),
    )

ASSET_TYPE = (
    (str(1), u"物理机"),
    (str(2), u"虚拟机"),
    (str(3), u"容器"),
    (str(4), u"网络设备"),
    (str(5), u"安全设备"),
    (str(6), u"其他")
    )


class UserInfo(models.Model):
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    login_method = models.CharField(max_length=128, null=True)
    def __unicode__(self):
        return self.username

    def __str__(self):
        return  self.username




class Idc(models.Model):
    ids = models.CharField(u"机房标识", max_length=255, unique=True)
    name = models.CharField(u"机房名称", max_length=255, unique=True)
    address = models.CharField(u"机房地址", max_length=100, blank=True)
    tel = models.CharField(u"机房电话", max_length=30, blank=True)
    contact = models.CharField(u"客户经理", max_length=30, blank=True)
    contact_phone = models.CharField(u"移动电话", max_length=30, blank=True)
    jigui = models.CharField(u"机柜信息", max_length=30, blank=True)
    ip_range = models.CharField(u"IP范围", max_length=30, blank=True)
    bandwidth = models.CharField(u"接入带宽", max_length=30, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, blank=True)
    #
    # def __unicode__(self):
    #     return self.name

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'数据中心'
        verbose_name_plural = verbose_name


class Cabinet(models.Model):
    idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(u"机柜", max_length=100)
    desc = models.CharField(u"描述", max_length=100, blank=True)
    # xxx= models.CharField(max_length=100,blank=True)


    # def __unicode__(self):
    #     return self.name
    #
    # def __str__(self):
    #     return self.name


class Asset(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
    asset_status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)
    hostname = models.CharField(max_length=50, verbose_name=u"主机名",)
    # Cabinet = models.ForeignKey(Cabinet, verbose_name=u"所在机柜", on_delete=models.SET_NULL, null=True, blank=True)
    ip = models.GenericIPAddressField(u"管理IP", max_length=15)
    # idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    sshPort = models.CharField(max_length=10,verbose_name=u'连接端口')
    position = models.CharField(u"所在位置", max_length=100, blank=True)
    cabinet = models.ForeignKey(Cabinet, verbose_name=u"所在机柜", on_delete=models.SET_NULL, null=True, blank=True)
    idc = models.ForeignKey(Idc, verbose_name=u"所在机柜", on_delete=models.SET_NULL, null=True, blank=True)
    account = models.ForeignKey(UserInfo,verbose_name=u"账号信息",  null=True, blank=True,max_length=80,on_delete=models.SET_NULL)


    def __unicode__(self):
        return self.hostname

    def __str__(self):
        return self.hostname
    #
    # def __repr__(self):
    #     return self.hostname





class AssetDetails(models.Model):
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE, verbose_name="设备名称", )
    # ip = models.GenericIPAddressField(u"管理IP", max_length=15)
    # account = models.ForeignKey(UserInfo, verbose_name=u"账号信息", on_delete=models.SET_NULL, null=True, blank=True)
    # idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    # Cabinet = models.ForeignKey(Cabinet, verbose_name=u"所在机柜", on_delete=models.SET_NULL, null=True, blank=True)
    other_ip = models.CharField( max_length=100, blank=True,verbose_name="其他ip")
    asset_no = models.CharField( max_length=50, blank=True,verbose_name="待定")
    # asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
    # status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)

    os = models.CharField( max_length=100, blank=True,verbose_name="操作系统")
    vendor = models.CharField( max_length=50, blank=True,verbose_name="设备厂商")
    init_up_time = models.DateField( auto_now_add=True,verbose_name="上架时间")
    up_time = models.DateTimeField( auto_now=True,verbose_name="修改时间")
    cpu_model = models.CharField( max_length=100, blank=True,verbose_name="CPU型号")
    cpu_num = models.CharField( max_length=100, blank=True,verbose_name="CPU数量")
    memory = models.CharField(max_length=30, blank=True,verbose_name="内存大小")
    disk = models.CharField( max_length=255, blank=True,verbose_name="硬盘信息")
    sn = models.CharField(max_length=60, blank=True,verbose_name="SN号码")
    position = models.CharField( max_length=100, blank=True,verbose_name="所在位置")
    memo = models.TextField( max_length=200, blank=True,verbose_name="备注信息")







class AssetGroup(models.Model):
    name = models.CharField(u"服务器组名", max_length=30, unique=True)
    desc = models.CharField(u"描述", max_length=100, blank=True)

    serverList = models.ManyToManyField(
            Asset,
            blank=True,
            verbose_name=u"所在服务器"
    )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name




class IpSource(models.Model):
    net = models.CharField(max_length=30)
    public_ip = models.CharField(max_length=30,null=True,)
    describe = models.CharField(max_length=30,null=True)

    def __unicode__(self):
        return self.net

    def __str__(self):
        return self.net



class InterFace(models.Model):
    name = models.CharField(max_length=30)
    vendor = models.CharField(max_length=30,null=True,verbose_name=u'供应商')
    bandwidth = models.CharField(max_length=30,null=True,verbose_name=u'带宽')
    tel = models.CharField(max_length=30,null=True,verbose_name=u'电话')
    contact = models.CharField(max_length=30,null=True)
    startdate = models.DateField()
    enddate = models.DateField()
    price = models.IntegerField(verbose_name=u'价格')

    def __unicode__(self):
        return self.name


    def __str__(self):
        return self.name







