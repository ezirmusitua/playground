function create_list_item(index) {
    const item = document.createElement("div");
    item.className = "list-item";
    item.innerText = `This is list item[${index}]`
    return item;
}

class List {
    constructor(visible_count = 15, anchor) {
        this.anchor = anchor
        this.all_items = Array.from({ length: 99999 }).map((_, i) => i + 1);
        this.visible_count = visible_count;
        this.current_page = 1;
        this.appended = [];
        this.top_hidden = [];
        this.bottom_hidden = [];
    }

    init() {
        for (const index of this.all_items.slice(0, this.visible_count * 3)) {
            const item = create_list_item(index)
            this.anchor.appendChild(item)
            const top_index = this.visible_count;
            if (index === top_index) {
                item.id = "list_top";
            }
            if (index === top_index + this.visible_count) {
                item.id = "list_bottom";
            }
            this.appended.push(item)
        }
    }

    load_up() {
        if (this.current_page === 1) {
            return;
        }
        this.current_page -= 1;
        const start = (this.current_page - 1) * this.visible_count;
        const end = this.current_page * this.visible_count
        const new_items = this.all_items.slice(start, end);
        let counter = 1;
        let new_top;
        for (const item of this.appended) {
            if (counter === 1) {
                item.id = "list_top";
                new_top = item;
            }
            if (counter === this.visible_count) {
                item.id = "list_bottom";
            }
            if (counter === this.visible_count * 2) {
                item.id = null;
            }
            if (counter > this.visible_count * 2 && counter <= this.visible_count * 3) {
                this.anchor.removeChild(item);
                // TODO: reuse generated item
                // this.top_hidden.push(item);
            }
            counter += 1;
        }
        this.appended = this.appended.slice(0, this.visible_count * 2)

        for (const index of new_items.reverse()) {
            const item = create_list_item(index);
            this.anchor.prepend(item);
            this.appended.unshift(item)
        }

        return new_top;
    }

    load_down() {
        this.current_page += 1;
        const start = (this.current_page + 1) * this.visible_count;
        const end = (this.current_page + 2) * this.visible_count
        const new_items = this.all_items.slice(start, end);
        let counter = 1;
        let new_bottom;
        for (const item of this.appended) {
            if (counter === this.visible_count) {
                item.id = null;
            }
            if (counter === this.visible_count * 2) {
                item.id = "list_top";
            }
            if (counter === this.visible_count * 3) {
                item.id = "list_bottom";
                new_bottom = item;
            }
            if (counter <= this.visible_count) {
                this.anchor.removeChild(item);
                // TODO: reuse generated item
                // this.top_hidden.push(item);
            }
            counter += 1;
        }
        this.appended = this.appended.slice(this.visible_count)

        for (const index of new_items) {
            const item = create_list_item(index);
            this.anchor.append(item);
            this.appended.push(item)
        }

        return new_bottom;
    }

    create_handler() {
        let prev_bottom_bounding_y = 0;
        let prev_bottom_inserecting = false;
        let prev_top_bounding_y = 0;
        let prev_top_intersecting = false;
        return (entries, observer) => entries.forEach((entry) => {
            if (entry.target.id === "list_bottom") {
                const is_scrolling_down = prev_bottom_bounding_y > entry.boundingClientRect.y
                if (is_scrolling_down && prev_bottom_inserecting && !entry.isIntersecting) {
                    // scrolling down and over bottom
                    const new_bottom = this.load_down();
                    if (new_bottom) {
                        observer.observe(new_bottom);
                    }
                }
                prev_bottom_bounding_y = entry.boundingClientRect.y;
                prev_bottom_inserecting = entry.isIntersecting;
            }

            if (entry.target.id === "list_top") {
                const is_scrolling_up = prev_top_bounding_y < entry.boundingClientRect.y
                if (is_scrolling_up && prev_top_intersecting && !entry.isIntersecting) {
                    const new_top = this.load_up();
                    if (new_top) {
                        observer.observe(new_top)
                    }
                }
                prev_top_intersecting = entry.isIntersecting;
                prev_top_bounding_y = entry.boundingClientRect.y;
            }
        });
    };
}


function index() {

    const list = new List(10, document.querySelector("#list_anchor"));
    list.init();
    const observer = new IntersectionObserver(list.create_handler(), {
        root: document.querySelector("#list_container"),
        threshold: 0.2
    });
    observer.observe(document.querySelector("#list_top"))
    observer.observe(document.querySelector("#list_bottom"))
}

index()
