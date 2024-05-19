export default class Building {
    constructor(sqft) {
        if (typeof sqft !== 'number') {
            throw new TypeError('Sqft must be a number')
        }
        this._sqft = sqft
    }

    get sqft() {
        return this._sqft;
    }

    set sqft(value) {
        if (typeof value !== 'number') {
            throw new TypeError('Sqft must be a number')
        }
        this._sqft = value
    }

    evacuationWarningMessage() {
        
    }
}