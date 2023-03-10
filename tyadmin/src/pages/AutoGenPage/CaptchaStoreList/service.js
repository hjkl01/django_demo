import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCaptchaStore(params) {
  return request('/api/xadmin/v1/captcha_store', {
    params,
  });
}
export async function removeCaptchaStore(params) {
  return request(`/api/xadmin/v1/captcha_store/${params}`, {
    method: 'DELETE',
  });
}
export async function addCaptchaStore(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/captcha_store', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCaptchaStore(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/captcha_store/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCaptchaStoreVerboseName(params) {
  return request('/api/xadmin/v1/captcha_store/verbose_name', {
    params,
  });
}
export async function queryCaptchaStoreListDisplay(params) {
  return request('/api/xadmin/v1/captcha_store/list_display', {
    params,
  });
}
export async function queryCaptchaStoreDisplayOrder(params) {
  return request('/api/xadmin/v1/captcha_store/display_order', {
    params,
  });
}


