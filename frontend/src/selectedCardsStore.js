import { writable } from 'svelte/store';

// Initialer Zustand ist ein leeres Set
export const selectedCardsStore = writable(new Set());