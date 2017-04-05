from django.db import models

from models.customer import CustomerModel, ReceiveAddressModel
from models.product import ProductModel
from models.seller import SellerModel


class OrderModel(models.Model):
    """订单模型"""
    UNPAY = 1
    UNSEND = 2
    UNRECEIVE = 3
    UNEVALUATE = 4
    FINISH = 5
    CANCEL = 6
    REFUND = 7
    AC_REFUND = 8
    STATUS = (
        (UNPAY, 'unpay'), (UNSEND, 'unsend'), (UNRECEIVE, 'unreceive'), (UNEVALUATE, 'unevaluate'), (FINISH, 'finish'),
        (CANCEL, 'cancel'), (REFUND, 'refund'), (AC_REFUND, 'accept-refund'))

    status = models.IntegerField(choices=STATUS, default=UNPAY)  # 订单产品状态
    customer = models.ForeignKey(CustomerModel, related_name="orders", on_delete=models.CASCADE)  # 买家
    recevieAddress = models.ForeignKey(ReceiveAddressModel, related_name="orders", on_delete=models.SET_NULL)  # 收货地址
    addTime = models.DateTimeField(auto_now_add=True)  # 订单添加时间
    payTime = models.DateTimeField(null=True)  # 付款时间
    cancelTime = models.DateTimeField(null=True)  # 订单取消时间
    customerMsg = models.TextField(null=True)  # 买家留言

    class Meta:
        db_table = 'order'


class OrderProductModel(models.Model):
    """订单商品模型"""
    UNSEND = 2
    UNRECEIVE = 3
    UNEVALUATE = 4
    FINISH = 5
    CANCEL = 6
    REFUND = 7
    AC_REFUND = 8
    STATUS = (
        (UNSEND, 'unsend'), (UNRECEIVE, 'unreceive'), (UNEVALUATE, 'unevaluate'), (FINISH, 'finish'),
        (CANCEL, 'cancel'), (REFUND, 'refund'), (AC_REFUND, 'accept-refund'))
    status = models.IntegerField(choices=STATUS, default=UNSEND)  # 订单产品状态
    order = models.ForeignKey(OrderModel, related_name="orderProducts", on_delete=models.CASCADE)  # 归属订单
    seller = models.ForeignKey(SellerModel, related_name="orderProducts", on_delete=models.SET_NULL)  # 卖家
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE)  # 商品
    addTime = models.DateTimeField(auto_now_add=True)  # 商品加入订单时间
    sellPrice = models.DecimalField(max_digits=10, decimal_places=2)  # 商品加入订单时价格
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 购买数量
    sendTime = models.DateTimeField(null=True)  # 发货时间
    receiveTime = models.DateTimeField(null=True)  # 收货时间
    evaluateTime = models.DateTimeField(null=True)  # 评价时间
    refundTime = models.DateTimeField(null=True)  # 退货时间
    ACRefundTime = models.DateTimeField(null=True)  # 商家接受退货时间
    refundReason = models.TextField(null=True)  # 退货理由
    evaluation = models.TextField(null=True)  # 订单评价
    eGrade = models.IntegerField(null=True)  # 商品评价

    class Meta:
        db_table = 'order_product'
