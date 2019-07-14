using System;
using System.Collections.Generic;
using System.Linq;
using LeanCloud.Realtime;
using UnityEngine;
using UnityEngine.UI;

public class Conversation : MonoBehaviour {
  // Start is called before the first frame update
  public Button loginBtn;
  public Button sendButton;
  public GameObject conversationGo;
  public GameObject messageItem;
  public InputField contentInput;
  public Transform messagesAnchor;
  private AVIMConversation _conv;
  private bool _sending;
  private int _loadedCount;

  void Start() {
    // 绑定按钮
    loginBtn.onClick.AddListener(Login);
    sendButton.onClick.AddListener(SendMessage);
  }

  async void Login() {
    try {
      // 登录
      await LeanCloudService.Instance.Login();
      // 初始化 Conversation, 结合 后端支持也可以做到加入已经存在的 Conversation
      _conv = await LeanCloudService.Instance.CreateConversation(
        new List<string> {"FooBar"},
        "Default Conversation",
        true
      );
      // 登录成功后显示对话框
      conversationGo.SetActive(true);
      loginBtn.gameObject.SetActive(false);
    }
    catch (Exception ex) {
      Debug.Log(ex.Message);
    }
  }

  async void SendMessage() {
    // 发送消息
    if (_conv == null) return;
    if (_sending) return;
    _sending = true;
    try {
      string content = contentInput.text;
      await LeanCloudService.Instance.SendMessage(_conv, content);
      // 清空输入框
      contentInput.Select();
      contentInput.text = "";
    }
    catch (Exception ex) {
      Debug.Log(ex.Message);
    }
    finally {
      _sending = false;
    }
  }

  // Update is called once per frame
  void Update() {
    if (_conv == null) return;
    var messages = LeanCloudService.Instance.GetMessages(_conv);
    if (_loadedCount >= messages.Count) return;
    var skipCount = _loadedCount;
    _loadedCount = messages.Count;
    // 加载最新的消息
    messages.Skip(skipCount).ToList().ForEach(message => {
      var go = Instantiate(messageItem, messagesAnchor);
      go.GetComponentInChildren<Text>().text = $"{message.FromClientId}: {message.TextContent}";
      _loadedCount += 1;
    });
  }
}