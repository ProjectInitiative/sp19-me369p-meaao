// @ts-ignore
const app = new Vue({
  el: '#app',
  data: {
    walkins: null,
    user: null,
    walkinInterval: null
  },
  methods: {
    getWalkins: function () {
      window.fetch('/walkins?result=json')
        .then(result => result.json().then(json => {
          this.walkins = json.walkins
          this.user = json.user
        }))
    },
    post: function (params) {
      this.clearInterval()
      this.walkins = null
      let data = new FormData()
      for (let param in params) {
        data.set(param, params[param])
      }
      let headers = new Headers();
      // @ts-ignore
      headers.append('X-CSRFToken', document.querySelector('input[name="csrfmiddlewaretoken"]').value)
      window.fetch('/walkins/', {
        method: 'POST',
        body: data,
        headers: headers
      }).then(() => {
        this.getWalkins()
        this.setInterval()
      })
    },
    hasGrant: function(grant) {
      return !!this.user && this.user.grants.includes(grant)
    },
    clearInterval: function () {
      clearInterval(this.walkinInterval)
    },
    setInterval: function () {
      this.walkinInterval = setInterval(this.getWalkins, 5000)
    },
    onInput: function () {
      this.clearInterval()
    },
    onChange: function (walkin) {
      let data = new FormData()
      let params = ['id', 'advisor_id', 'comments']
      data.set('action', 'walkin_save')
      for (let param in params) {
        data.set(params[param], walkin[params[param]])
      }
      let headers = new Headers();
      // @ts-ignore
      headers.append('X-CSRFToken', document.querySelector('input[name="csrfmiddlewaretoken"]').value)
      window.fetch('/walkins/', {
        method: 'POST',
        body: data,
        headers: headers
      }).then(() => {
        this.getWalkins()
        this.setInterval()
      })
    },
  },
  mounted: function () {
    this.getWalkins()
    this.setInterval()
  }
})

// @ts-ignore
var $ = window.$ || $;
$(document).ready(function () {
  let templateRender = state => {
    if (!state.id)  return state.text
    return $('<span>')
      .append($('<b>').text(state.data[1]).css('font-weight', 'bold'))
      .append($('<span>').text(state.data[0]).css('float', 'right'));
  }
  // @ts-ignore
  $('#student').select2({
    ajax: {
      url: '?search_student',
      dataType: 'json'
    },
    width: '100%',
    minimumInputLength: 2,
    templateResult: templateRender,
    templateSelection: templateRender,
    selectOnClose: true,
    delay: 200
  }).on("select2:open", function () {
    $('.select2-container').addClass('select2-container--open');
    $('.select2-search__field').focus();
  }).on("select2:close", function () {
    setTimeout(function() {
      $('.select2-container').removeClass('select2-container--open');
      $('.select2-search__field').blur();
    }, 1);
  });
})
