function tmpl(strings, ...keys) {
  return (function (...values) {
    const dict = values[values.length - 1] || {};
    const result = [strings[0]];
    keys.forEach(function (key, i) {
      const value = Number.isInteger(key) ? values[key] : dict[key];
      result.push(value, strings[i + 1]);
    });
    return result.join('');
  });
}

const DOC_SECTION_TMPL = tmpl`### ${'action_name'}\n\n  
\`\`\`js
await api.transact({
  actions: [{
    account: 'eosio',
    name: '${'action_name'}',
    authorization: [{
      actor: <account_name>,
      permission: <permission_name>,
    }],
    data: {
      ${'fields'}
    }
  }]
}, {
  blocksBehind: 3,
  expireSeconds: 30,
})
\`\`\`
`;

function joinFields(fields, indent = 6) {
  let res = '';
  for (const field of fields) {
    res += `${field.name}: <${field.type}>, \n${' '.repeat(indent)}`;
  }
  return res;
}


function generate(structs_or_abi) {
  let structs = structs_or_abi;
  if (structs_or_abi.version) {
    structs = structs_or_abi.structs;
  }
  return structs.map(st => DOC_SECTION_TMPL({
    action_name: st.name,
    fields: joinFields(st.fields)
  })).join('\n\n');
}

function cmd() {
  const fpath = process.argv[2] || './abi.json';
  const structsOrAbi = require(fpath);
  const docStr = generate(structsOrAbi);
  console.info(docStr);
}

cmd();

