/**
 * Created by zihang on 2017/4/19.
 */
// 实例化编辑器
KindEditor.ready(function(K) {
	K.create('textarea[name=text_content]', {
    //create 括号中的内容为获取textarea的这个文本域 你可以使用CSS选择器获取
    // 如：create(#xxx) #xxx 对应 textarea id= 'xxx' ,这个id在当前页面只能存在1个
    // 或create(textarea) 条件是当前页面当中只存在1个 textarea
	//花括号存放富文本配置信息 如 width:600px
		height:'300px;',
	});
});
