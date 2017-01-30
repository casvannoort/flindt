import axios from 'axios';
import { API_URL } from '../constants/constants';

// Fetch feedback lists as sender
export const FETCH_FEEDBACK_AS_SENDER = 'FETCH_FEEDBACK_AS_SENDER';

// Fetch feedback lists as receiver
export const FETCH_FEEDBACK_AS_RECEIVER = 'FETCH_FEEDBACK_AS_RECEIVER';

// Fetch feedback object
export const FETCH_FEEDBACK = 'FETCH_FEEDBACK';
export const EDIT_FEEDBACK = 'EDIT_FEEDBACK';

// Post new feedback
export const CREATE_FEEDBACK = 'CREATE_FEEDBACK';

export const CLEAN_FEEDBACK = 'CLEAN_FEEDBACK';

// Test URL to get data as a json to show in our view.
const ROOT_URL = `${API_URL}/api/v1`;

export function fetchFeedbackAsSender(accessToken) {
    const request = axios({
        method: 'GET',
        url: `${ROOT_URL}/users/feedback-as-sender/`,
        headers: {Authorization: `Bearer ${accessToken}`},
    });

    return {
        type: FETCH_FEEDBACK_AS_SENDER,
        payload: request,
    };
}

export function fetchFeedbackAsReceiver(accessToken) {
    const request = axios({
        method: 'GET',
        url: `${ROOT_URL}/users/feedback-as-receiver/`,
        headers: {Authorization: `Bearer ${accessToken}`},
    });

    return {
        type: FETCH_FEEDBACK_AS_RECEIVER,
        payload: request,
    };
}

export function editFeedback(props, accessToken) {
    const request = axios({
        method: 'PATCH',
        data: props,
        url: `${ROOT_URL}/feedbacks/${props.id}/`,
        headers: {Authorization: `Bearer ${accessToken}`},
    });

    return {
        type: EDIT_FEEDBACK,
        payload: request,
    };
}

export function fetchFeedback(accessToken, id) {
    const requestFeedback = axios({
        method: 'GET',
        url: `${ROOT_URL}/feedbacks/${id}/`,
        headers: {Authorization: `Bearer ${accessToken}`},
    });

    return {
        type: FETCH_FEEDBACK,
        payload: requestFeedback,
    };
}


export function cleanFeedback() {
    return {
        type: CLEAN_FEEDBACK,
    };
}